import pandas as pd

def process_data(pdf_list, get_serial_range):
    # Create a dummy dataframe
    df = pd.DataFrame(columns=['Sr. No.', 'Item No', 'Quantity', 'Unit', 'Rate'])

    for arr in range(len(pdf_list)):
        for i in get_serial_range:
            if pdf_list[arr][0] == i:
                data_to_append = []
                count = 0
                for value in pdf_list[arr][0:]:
                    if value:
                        if count == 0:
                            data_to_append.append(str(value))
                        if count == 1 or count == 2 or count == 3 or count == 4:
                            data_to_append.append(value)
                        count += 1
                        if count == 5:
                            break  # Stop after collecting 5 non-empty values

                # Pad with empty strings if there are fewer than 5 values
                while len(data_to_append) < 5:
                    data_to_append.append("")

                # Append the data to the DataFrame
                df.loc[len(df)] = data_to_append

    # Check if 5th column is the product of 2nd and 4th columns
    for index, row in df.iterrows():
        try:
            if round(float(row['Rate'].replace(',', '')), 2) == round(round(float(row['Item No'].replace(',', '')), 2) * round(float(row['Unit'].replace(',', '')), 2), 2):
                # Perform the left shift operation
                df.at[index, 'Rate'] = row['Unit']
                df.at[index, 'Unit'] = row['Quantity']
                df.at[index, 'Quantity'] = row['Item No']
                df.at[index, 'Item No'] = ''
        except ValueError:
            # Handle non-numeric values if needed
            pass

    # Add rupee icon to the 'Rate' column
    # df['Rate'] = "₹ " + df['Rate']

    return df
