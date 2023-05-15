import json
import os
import shutil
from pyhtml2pdf import converter
from simplegmail import Gmail
from simplegmail.query import construct_query
from python.document_processing.document_processing import extract_text_from_pdf
from python.claude.claude import claude_api
from pprint import pprint
from Levenshtein import ratio
from re import findall
from decimal import Decimal

# shutil.copy("gmail_token_symlink.json", "/tmp/gmail_token.json", follow_symlinks=True)
# shutil.copy("gmail_token_symlink.json", "gmail_token.json", follow_symlinks=True)
# gmail = Gmail()

# # Unread messages in your inbox
# query_params = {
#     "newer_than": (2, "day"),
#     "unread": True,
# }

# messages = gmail.get_unread_inbox(query=construct_query(query_params))

# # Print them out!
# for message in messages:
#     print("To: " + message.recipient)
#     print("From: " + message.sender)
#     print("Subject: " + message.subject)
#     print("Date: " + message.date)
#     print("Preview: " + message.snippet)
#     print("Message Body: " + message.plain)  # or message.html
#     if message.attachments:
#         for attm in message.attachments:
#             print('File: ' + attm.filename)
#             base_file_name: str = attm.filename.strip(".html")
#             html_path: str = f"/tmp/{attm.filename}"
#             pdf_path: str = f"/tmp/{base_file_name}.pdf"

#             attm.save(filepath=f"/tmp/{attm.filename}", overwrite=True)
#             # htmpath = os.path.abspath(html_path)
#             converter.convert(f"file:///{html_path}", pdf_path)
#             po_text: str = extract_text_from_pdf(pdf_path)
#             os.remove(pdf_path)
#             os.remove(html_path)

#             question = "Given the following PO data, what items did they oder? Only provide name, price, quantity in a table format pretty"
#             gpt_response: str = claude_api(po_text, question)
#             print(gpt_response)
fail = 0
success = 0
for i in range(303,304):
    purchase_order_path: str = f"/tmp/bp2.6/{i}.pdf"
    answers_json_path: str = f"/tmp/bp2.6/{i}.json"
    # base_file_name: str = attm.filename.strip(".html")
    # html_path: str = f"/tmp/{attm.filename}"
    # pdf_path: str = f"/tmp/{base_file_name}.pdf"

    # attm.save(filepath=f"/tmp/{attm.filename}", overwrite=True)
    # # htmpath = os.path.abspath(html_path)
    # converter.convert(f"file:///{html_path}", pdf_path)

    # os.remove(pdf_path)
    # os.remove(html_path)
    #po_text: str = extract_text_from_pdf(purchase_order_path)
    po_text: str = f'''
Purchase Order #            742703562-1

Purchase Order Date    11/07/2022

Payment Terms             Net 60
eMolecules, Inc
3430 Carmel Mountain Road, Suite 250
San Diego, CA 92121






Supplier                                                         Bill To                                                             Ship To

S81 Broadpharm                                            Email:                                                             ATTN: RYO TAMURA Z-2045 / 
6625 Top Gun St. Suite 103                            (accounts.payable@emolecules.com)            C22160441
San Diego CA 92121                                                                                                              MSKCC
United States                                                  OR                                                                  408-20
408 E 69TH ST
Attn: Accounts Payable                                   NEW YORK, NY 10021
Ref #: 742703562-1                                        United States
eMolecules, Inc                                             Phone: +1 724 517-2327
3430 Carmel Mountain Road, Suite 250
San Diego, CA 92121



Special Order Instructions



Customer PO (Must be referenced on Package):                          C22160441

Ship Via:                                                                                            SEE PO DETAIL

Incoterms / Terms of Delivery:                                                        DAP

eMolecules Purchasing Contact:                                                    (supplier@emolecules.com)

Summary of Cost

TOTAL Retail Price:                                                                          $965.00

TOTAL eMolecules Invoice Price:                                                    $908.00

Currency:                                                                                          USD



Date: 11/07/2022 Customer Reference: C22160441 eMolecules Reference: 742703562-1 TO ENSURE PO RECEIVED BY 
VENDOR, ALL ORDERS MUST BE CONFIRMED TO EMAIL: SUPPLIER@EMOLECULES.COM OR FAX AT 858-764-1917 DO 
NOT SEND INVOICE(S) TO PROCUREMENT To receive payment from your purchase order (PO), mail or email 
(accounts.payable@emolecules.com) a document clearly marked ©INVOICE© to the © Bill To© address provided at the top of the PO 
with the following information clearly listed: Description of service(s) and/or goods provided, PO number, amount owed and name 
and address payment is to be sent to. This will help facilitate a quick payment to you for services rendered. All invoice or billing 
related questions should be referred to eMolecules© Accounting Department at 858.368.8653.



Additional Shipping Notes:

Salt Alternatives When Applicable:                                                     Email supplier@emolecules.com w/ alternatives or purity 
concerns.

Preferred Shipment Method:                                                              FedEx Standard Overnight (never First Overnight) or
International Priority. Do not use FedEx boxes.



742703562-1                                                                                                                                                                                                            1 of 7
Purchase Order #            742703562-1

Purchase Order Date    11/07/2022

Payment Terms             Net 60
eMolecules, Inc
3430 Carmel Mountain Road, Suite 250
San Diego, CA 92121

Shipment Carrier Instruction : SHIP VIA FEDEX                           BILL THIRD PARTY eMolecules FedEx Account 145513502

Shipment within UK Carrier Instruction : SHIP VIA DHL               BILL THIRD PARTY eMolecules DHL Account 418225059

Back Ordered Sample:

Latest Acceptab                         le Ship date*:                                                            Email supplier@emolecules.com

1) Please include SAFETY DATA SHEETS (SDSs) for all items WITH shipment and e-mail to lab@emolecules.com. 
2) Send all shipment and tracking information along with the Excel info request form to: shipping@emolecules.com. 
3) IF the QUANTITY below is GREATER THAN ONE, the customer would like to order multiples of the pack size that is listed in the 
adjacent column.



Tier                                     List Unit 
Catalog ID      Description                   Quantity   Pack Size                            Due Date                              Unit Price    Total Price
Number                              Price

BP-23668        Mal-PEG4-Val-Cit-                   1    100mg           Tier 11/09/202   $950.00              $893.00         $893.00
PAB-PNP                                                                Accelerate   2
2112738-09-5                                                         d
MFCD30828694

Shipping and   1                          Tier    $15.00                  $15.00           $15.00
Handling                                                                 Accelerate
d



                                                                                                                                                                       Total                      $908.00



eMolecules Purchase Order Number: 742703562-1    
'''

    print("PO text")
    print(po_text)

    prompt =f'''Here's some information from a Purchase Order: {po_text}.
    4 or more spaces between text indicates lines from the PDF. Thus, closely
    grouped text should be considered one entity and read as one entity when answering questions.
    The Bill to address should not include an email. The Ship to address should not include an email.
    Double check that the Bill to address and Ship to address contains a country, city, zip code, street address.
    You are an agent that is creating an invoice from this purchase order,
    tasked with identifying the ship to address, bill to address,
    details regarding items ordered including name, price and quantity,
    and total cost. If there's a unit price and a price, use the cheaper price
    as the answer. Ensure prices added up in Item order details add up to total price
    If any of these items are not found, answer should be N/A.
    For the Item order details, make each response a separate row.
    Fill in the following. Each entry should not have newlines.
    For Item Order Details, keep appending additional rows until all item order
    details have been added.

    Ship to address; <your answer to Ship to address>,
    Bill to address; <your answer to Bill to address>,
    Total Cost; <your answer to total cost>,
    Item Order Details; [<first item order name>,<first item order price>,<first item order quantity>]'''
    gpt_response: str = claude_api(prompt)
    tot_cost = 0.0
    print("GPT RESP")
    pprint(gpt_response)
    print("GPT RESP end")
    results = {
        "Ship to address": "N/A",
        "Bill to address": "N/A",
        "Total Cost": 0.0,
        "Item Order Details": []
    }
    gpt_response_lines = gpt_response.split("\n")
    try:
        while len(gpt_response_lines) > 0:
            cur_line = ""
            read_entire_answer = False
            if "[" in gpt_response_lines[0]:
                while len(gpt_response_lines) > 0:
                    cur_line += gpt_response_lines.pop(0)
                item_order_details_list: list = findall(r'\[(.*?)\]', cur_line)
                for item_order_detail in item_order_details_list:
                    name, cost, qty = item_order_detail.split(",")
                    item_order_detail = {"name": name,
                                         "cost": "{:.2f}".format(float(cost.replace("$",""))) ,
                                         "qty": int(qty.replace("$",""))}
                    results["Item Order Details"] += [item_order_detail]
            else:
                num_semicolons = 0
                while len(gpt_response_lines) > 0 and num_semicolons < 2:
                    if ";" in gpt_response_lines[0]:
                        num_semicolons += 1
                    if num_semicolons >= 2:
                        break
                    cur_line += gpt_response_lines.pop(0)

                key, val = cur_line.split(";")
                results[key.strip(" ").strip("'").strip('"')] = val.strip("'").strip("'").strip('"').strip("\n")

    except Exception as e:
        print(f"EXCEPTION={e}")



    with open(answers_json_path, 'r') as f:
        ground_truth = json.load(f)
        total = len(ground_truth["What are the costs per item"])

        item_in = 0
        ground_truth_cost_set = set(ground_truth["What are the costs per item"])
        for item_detail in results["Item Order Details"]:
            if item_detail["cost"] in ground_truth_cost_set:
                item_in += 1

        ship_diff = ratio(results["Ship to address"], ground_truth["What is the shipping address"])
        bill_diff = ratio(results["Bill to address"], ground_truth["What is the billing address"])

        print(f"ship_diff={ship_diff}, bill_diff={bill_diff}")
        pprint("RESULTS")
        pprint(results)

        if total//2 > item_in or (bill_diff < 0.6 and ship_diff < 0.6):
            fail += 1
            print("_"*100)
            print("FAIL")
            pprint(ground_truth)
            print("FAIL")
            print("_"*100)
        else:
            success += 1


print(f"total fail = {fail}")
print(f"total success = {success}")