import pandas as pd
import numpy as np
import sys

def validate_l2(l1, l2):
    conditions = []
    len_arr = min(len(l1), len(l2))
    cnt_check = len(l1) == len(l2)

    for i in range(len_arr):
        conditions.append(
            (l2.at[i, 'order_type'] == l1.at[i, 'product_type']) or (l2.at[i, 'product_type'] == 'rule'),
            l2.at[i, 'dim_group_id'] == l1.at[i, 'dim_group_id'],
            l2.at[i, 'order_no'] == l1.at[i, 'order_no'],
            l2.at[i, 'dim_bookingdate_id'] == l1.at[i, 'dim_bookingdate_id'],
            l2.at[i, 'dim_store_id'] == l1.at[i, 'dim_store_id'],
            l2.at[i, 'service_fee_code'] == l1.at[i, 'product_name'],
            l2.at[i, 'dim_customer_id'] == l1.at[i, 'dim_customer_id'],
            l2.at[i, 'dim_language'] == l1.at[i, 'dim_language'],
            l2.at[i, 'dim_totals_currency'] == l1.at[i, 'dim_totals_currency'],
            l2.at[i, 'dim_status_id'] == l1.at[i, 'dim_status_id'],
            l2.at[i, 'phone'] == l1.at[i, 'phone'],
            l2.at[i, 'payment_amount'] == l1.at[i, 'payment_amount'],
            l2.at[i, 'discount_amount'] == l1.at[i, 'discount_amount'],
            # l2.at[i, 'service_fee_amount'] == l1.at[i, 'service_fee_amount'],
            l2.at[i, 'base_amount'] == l1.at[i, 'base_amount'],
            l2.at[i, 'inputvat'] == l1.at[i, 'inputvat'],
            l2.at[i, 'outputvat'] == l1.at[i, 'outputvat'],
            l2.at[i, 'product_vat'] == l1.at[i, 'product_vat'],
            l2.at[i, 'selling_price'] == l1.at[i, 'selling_price'],
            l2.at[i, 'selling_price_vat'] == l1.at[i, 'selling_price_vat'],
            l2.at[i, 'ibv'] == l1.at[i, 'ibv'],
            l2.at[i, 'iov_usd'] == l1.at[i, 'ibv'] * l1.at[i, 'conversion_rate_usd'],
            l2.at[i, 'gbv'] == l1.at[i, 'gbv'],
            l2.at[i, 'gbv_usd'] == l1.at[i, 'gbv'] * l1.at[i, 'conversion_rate_usd']
        )

    return np.all(conditions, axis=0), cnt_check

def main(input_path_l1, input_path_l2, output_path):
    l1_data = pd.read_csv(input_path_l1)
    l2_data = pd.read_csv(input_path_l2)

    validation_result, cnt_check = validate_l2(l1_data, l2_data)

    qa_report = pd.DataFrame({
        'Test Case': ['Validation of L2 Output'],
        'Date': [pd.Timestamp.now()],
        'Test Summary': ['The L2 table was validated against the specified business requirements.'],
        'Results': [f'Test {"Passed" if validation_result.all() else "Failed"}'],
        'Conclusion': [f'The L2 table {"" if validation_result.all() else "doesn\'t"} meet the business requirements based on the provided logic.'],
        'l1 count match l2 count ?': [cnt_check]
    })

    print("QA Report:")
    print(qa_report.to_string(index=False))
    
    # Save QA Report to CSV
    qa_report.to_csv(output_path, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py input_path_l1 input_path_l2 output_path")
    else:
        input_path_l1 = sys.argv[1]
        input_path_l2 = sys.argv[2]
        output_path = sys.argv[3]
        main(input_path_l1, input_path_l2, output_path)
