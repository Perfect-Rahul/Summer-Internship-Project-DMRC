# Summer-Internship-Project-DMRC
Contains the project "Automated Threat Intelligence Pipeline for Firewall Security" which was done by me in summer internship second year at Delhi Metro Rail Corporation.

• Built an automated system to extract, parse, validate, and integrate cyber threat intelligence (IoCs) directly from
email advisories into firewall blocklists.

• Parsed structured and unstructured emails to extract IoCs such as IPs, Domains, URLs, and File Hashes.

• Integrated with firewall via APIs to continuously update threat signatures without manual effort.

• Developed a GUI dashboard for IOC handling, monitoring, audit logs, and exception management.

• Added automated email reporting, data retention & cleanup, and credential encryption for secure operation.

1. api_pusher.py: pushes IOC data from the database to the firewall.
2. auto_email_parser.py: extracts IOC data from emails automatically.
3. db.py: database connector which connects to the database and pushes data there.
4. email_reporter.py: reports daily about the total threats extracted and their information through mail.
5. interface.py: For making GUI to handle this whole process.
6. mock_firewall.py: mock firewall made to test api pushing to it.
7. nightly_cleanup.py: Cleans old data from the database system.
