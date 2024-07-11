
import csv
from io import StringIO

def send_email(ses_client, from_email, to_email, subject, body, attachment_content, attachment_name):
    response = ses_client.send_raw_email(
        Source=from_email,
        Destinations=[to_email],
        RawMessage={
            'Data': create_email_message(from_email, to_email, subject, body, attachment_content, attachment_name)
        }
    )
    return response

def create_email_message(from_email, to_email, subject, body, attachment_content, attachment_name):
    import email
    import email.mime.application

    msg = email.mime.multipart.MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Attach the body with the msg instance
    msg.attach(email.mime.text.MIMEText(body))

    # Attachment
    part = email.mime.application.MIMEApplication(attachment_content, Name=attachment_name)
    part['Content-Disposition'] = f'attachment; filename="{attachment_name}"'
    msg.attach(part)

    return msg.as_string()

def publish_sns(sns_client, topic_arn, subject, message):
    response = sns_client.publish(
        TopicArn=topic_arn,
        Subject=subject,
        Message=message
    )
    return response

def transform_onix_to_csv(onix_message):
    # Convert ONIXMessage to CSV format
    output = StringIO()
    csv_writer = csv.writer(output)

    # Write CSV headers
    csv_writer.writerow([
        'Record Reference', 'Notification Type', 'Product Identifier', 'Product Form',
        'Title', 'Author', 'Publisher', 'Publication Date', 'Language', 'Number of Pages', 'Price'
    ])

    # Write CSV data
    for product in onix_message.products:
        csv_writer.writerow([
            product.record_reference, product.notification_type, product.product_identifier, product.product_form,
            product.title, product.author, product.publisher, product.publication_date, product.language,
            product.number_of_pages, product.price
        ])

    return output.getvalue()
