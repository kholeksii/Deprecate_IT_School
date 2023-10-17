import csv

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     with open('emails.csv', 'w', newline='') as csv_emails_file:
#         csv_writer = csv.writer(csv_emails_file)
#
#         for line in csv_reader:
#             csv_writer.writerow([line['email']])

with open('names.csv', 'r') as csv_file:
   csv_reader = csv.reader(csv_file)

   with open('emails.csv', 'w', newline='') as csv_emails_file:
       csv_writer = csv.writer(csv_emails_file)

       for line in csv_reader:
           print(line[2])
           csv_writer.writerow([line[2]])
