import os
from google.cloud import bigquery
from flask import jsonify
from dotenv import load_dotenv

load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

client = bigquery.Client()

def procedure_count_rows():

    sql_query = """
    SELECT count(*) total_rows FROM `bigquery-public-data.cms_synthetic_patient_data_omop.procedure_occurrence` 
    """

    results = client.query(sql_query).result()

    for row in results:
        #print(row.total_rows)
        return jsonify(
            {
                'data': row.total_rows,
                'success': True
            }
        )


def procedure_count_persons_for_n_last_date(n):

    sql_query = f"""
    SELECT  count(distinct person_id) count_persons
    FROM `bigquery-public-data.cms_synthetic_patient_data_omop.procedure_occurrence` 
    where procedure_dat in (
        select distinct procedure_dat
        from `bigquery-public-data.cms_synthetic_patient_data_omop.procedure_occurrence`
        order by procedure_dat desc
        limit {n}
    )    
    """

    results = client.query(sql_query).result()

    for row in results:
        #print(row.count_persons)
        return jsonify(
            {
                'data': row.count_persons,
                'n': n,
                'success': True
            }
        )
    
if __name__ == '__main__':
    procedure_count_rows()
    procedure_count_persons_for_n_last_date(3)

