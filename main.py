# # ./main.py

# from module.get_serials import getSerials
# from module.generate_serials_range import generateSerialsRange
# from module.readPdf import read_PDF, get_Pages, pdf_List

# import pandas as pd

# # Get the First and Last Serial Number from SOR
# get_serial_no = getSerials()

# # Generate the Serial Range with Zeros in front
# get_serial_range = generateSerialsRange(
#     get_serial_no[0], get_serial_no[1], 10, 5)

# # Read Pdf
# pdf = read_PDF('../TENDER.pdf')
# total_pages = get_Pages(pdf)
# print('No of pages: ', total_pages)

# pdf_list = pdf_List(pdf, total_pages)

# # create a dummy dataframe
# df = pd.DataFrame(columns=['Sr. No.', 'Item No', 'Quantity', 'Unit', 'Rate'])

# for arr in range(len(pdf_list)):

#     for i in get_serial_range:

#         if pdf_list[arr][0] == i:
#             data_to_append = []
#             count = 0
#             for value in pdf_list[arr][0:]:
#                 if value:
#                     if count == 0:
#                         data_to_append.append(str(value))
#                     if count == 1 or count == 2 or count == 3 or count == 4:
#                         data_to_append.append(value)
#                     count += 1
#                     if count == 5:
#                         break  # Stop after collecting 5 non-empty values

#             # Pad with empty strings if there are fewer than 5 values
#             while len(data_to_append) < 5:
#                 data_to_append.append("")

#             # Append the data to the DataFrame
#             df.loc[len(df)] = data_to_append


# # Check if 5th column is the product of 2nd and 4th columns
# for index, row in df.iterrows():
#     try:
#         if round(float(row['Rate'].replace(',', '')),2) == round(round(float(row['Item No'].replace(',', '')),2) * round(float(row['Unit'].replace(',', '')),2),2):
#             # Perform the left shift operation
#             df.at[index, 'Rate'] = row['Unit']
#             df.at[index, 'Unit'] = row['Quantity']
#             df.at[index, 'Quantity'] = row['Item No']
#             df.at[index, 'Item No'] = ''
            
            
#     except ValueError:
#         # Handle non-numeric values if needed
#         pass


# # Add rupee icon to the 'Rate' column
# df['Rate'] = "₹ " + df['Rate']


# # # Export the DataFrame to an Excel file
# excel_file = 'b.xlsx'
# df.to_excel(excel_file, index=False)


from module.get_serials import getSerials
from module.generate_serials_range import generateSerialsRange
from module.readPdf import read_PDF, get_Pages, pdf_List
from module.data_processing import process_data

# Get the First and Last Serial Number from SOR
get_serial_no = getSerials()

# Generate the Serial Range with Zeros in front
get_serial_range = generateSerialsRange(
    get_serial_no[0], get_serial_no[1], 10, 5)

# Read Pdf
pdf = read_PDF('../TENDER.pdf')
total_pages = get_Pages(pdf)
print('No of pages: ', total_pages)

pdf_list = pdf_List(pdf, total_pages)

# Process data using the function from data_processing module
df = process_data(pdf_list, get_serial_range)

# Export the DataFrame to an Excel file
excel_file = 'b.xlsx'
df.to_excel(excel_file, index=False)

print(f"Excel file '{excel_file}' has been created.")
