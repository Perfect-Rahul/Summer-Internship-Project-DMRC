def fetch_threats_from_email():
    import imaplib, email, re
    from db import insert_ips, insert_domains, insert_hashes
    from api_pusher import push_ips, push_domains, push_hashes

    EMAIL = "rahulpanwar58788@gmail.com"
    PASSWORD = "vxlv zjfv rnzc zgry"
    IMAP_SERVER = "imap.gmail.com"
    PROCESSED_FOLDER = "Processed"

    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select("INBOX")

    # Fetch the last 20 emails (or more if needed)
    status, messages = mail.search(None, 'ALL')
    mail_ids = messages[0].split()[-20:]  # Last 20 emails

    all_ips, all_domains, all_hashes = [], [], []
    logs = []

    for mail_id in reversed(mail_ids):
        try:
            _, msg_data = mail.fetch(mail_id, "(RFC822)")
            raw_msg = msg_data[0][1]
            msg = email.message_from_bytes(raw_msg)

            subject = msg['Subject']
            if subject is None or "Threat Advisory" in subject:
                subject_display = subject or "(No Subject)"
                logs.append(f"📧 Processing email {mail_id.decode()} - Subject: {subject_display}")

                # Extract plain text content
                email_body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            email_body = part.get_payload(decode=True).decode(errors='ignore')
                            break
                else:
                    email_body = msg.get_payload(decode=True).decode(errors='ignore')

                data = email_body.replace("[.]", ".")

                # IOC presence check
                if not re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', data) and \
                        not re.search(r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b', data) and \
                        not re.search(r'\b[a-fA-F0-9]{40}\b', data):
                    logs.append(f"⚠️ Skipping email {mail_id.decode()} - No IOCs found in content.")
                    continue

                # Extract and push
                ips = list(set(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', data)))
                domains = list(set(re.findall(r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b', data)))
                hashes = list(set(re.findall(r'\b[a-fA-F0-9]{40}\b', data)))

                all_ips += ips
                all_domains += domains
                all_hashes += hashes

                insert_ips(ips)
                insert_domains(domains)
                insert_hashes(hashes)

                push_ips(ips)
                push_domains(domains)
                push_hashes(hashes)

                mail.copy(mail_id, PROCESSED_FOLDER)
                mail.store(mail_id, '+FLAGS', '\\Deleted')
                mail.expunge()

                logs.append(
                    f"✅ Processed email {mail_id.decode()}: {len(ips)} IPs, {len(domains)} Domains, {len(hashes)} Hashes")
                logs.append(f"📦 Moved to {PROCESSED_FOLDER}")

        except Exception as e:
            logs.append(f"❌ Error processing email {mail_id.decode()}: {e}")

    mail.logout()
    logs.append(
        f"✅ Total extracted: {len(set(all_ips))} IPs, {len(set(all_domains))} Domains, {len(set(all_hashes))} Hashes.")
    return list(set(all_ips)), list(set(all_domains)), list(set(all_hashes)), logs
