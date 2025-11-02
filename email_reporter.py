import smtplib
from email.message import EmailMessage

SENDER = "rahulpanwar58788@gmail.com"
APP_PASSWORD = "vxlv zjfv rnzc zgry"
RECEIVER = "rahul.panwar_btech23@gsv.ac.in"  # or security-team@example.com
## CC_LIST = ["security1@example.com", "soc@example.com", "teamlead@example.com"]

def send_report_email(ips, domains, hashes):
    msg = EmailMessage()
    msg['Subject'] = "✅ Threat Feed Push Report - Today"
    msg['From'] = SENDER
    msg['To'] = RECEIVER
    ## msg['Cc'] = ", ".join(CC_LIST)

    msg.set_content(create_email_body(ips, domains, hashes))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER, APP_PASSWORD)
            smtp.send_message(msg)
            print("📤 Email report sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email report: {e}")

def create_email_body(ips, domains, hashes):
    body = f"""Hello,

Here is the summary of threats pushed to the firewall today:

Total IPs: {len(ips)}
Total Domains: {len(domains)}
Total Hashes: {len(hashes)}

--- IPs ---
{chr(10).join(ips) if ips else 'None'}

--- Domains ---
{chr(10).join(domains) if domains else 'None'}

--- Hashes ---
{chr(10).join(hashes) if hashes else 'None'}

Regards,  
Threat Automation System  
"""
    return body
