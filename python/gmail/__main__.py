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
for i in range(303,315):
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
    po_text:str = (os.popen(f"./python/gmail/TextExtractionBinaryDarwin {purchase_order_path}").read())[0:20000]
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
    # print("GPT RESP")
    # pprint(gpt_response)
    # print("GPT RESP end")
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


        if total//2 > item_in or (bill_diff < 0.6 and ship_diff < 0.6):
            fail += 1
            print("_"*100)
            print("FAIL")
            print(f"ship_diff={ship_diff}, bill_diff={bill_diff}")
            pprint("GROUND TRUTH")
            pprint(ground_truth)
            pprint("ACTUAL GPT RESULTS")
            pprint(results)
            print("FAIL")
            print("_"*100)
        else:
            success += 1


print(f"total fail = {fail}")
print(f"total success = {success}")



# dir_path="/Users/ryang/Downloads/waterloo-resume"
# for filename in os.listdir(dir_path):
#     # Construct the full file path
#     if filename == ".DS_Store":
#         continue
#     resume_path = os.path.join(dir_path, filename)
#     print(resume_path)
#     po_text:str = (os.popen(f"./python/gmail/TextExtractionBinaryDarwin \"{resume_path}\"").read())#[20:9600]
#     # print("PO text")
#     # print(po_text)

#     prompt =f'''Here's some information from a resume: {po_text}.
#     You are a resume screener. Please fill in the following lines below
#     and fill in with N/A if not found. The student year should conform to the following
#     2A,2B,3A,3B,4A,4B. IF GPA is not present, Sum all the Term Average and then provide an average
#     Name:
#     Year: <Student Year>
#     GPA_Average_CS_Courses: <student GPA>
#     GPA_Average_Math_Courses: <student GPA>
#     GPA: <student GPA>
#     past co-op ratings: (<co-op company> <co-op ratings>)
#     '''
#     gpt_response: str = claude_api(prompt)
#     tot_cost = 0.0
#     print("GPT RESP")
#     pprint(gpt_response)
#     print("GPT RESP end")

