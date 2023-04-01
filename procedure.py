import os
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'website-281615-d7069b7166e0.json'

client = bigquery.Client()

def procedure_count_rows():
    sql_query = """
    SELECT count(*) total_rows FROM `bigquery-public-data.cms_synthetic_patient_data_omop.procedure_occurrence` 
    """

    results = client.query(sql_query).result()

    for row in results:
        #print(row.total_rows)
        return f'Total rows in the procedure_occurrence table is {row.total_rows}'


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
        return f'Total number of persons for the last {n} procedure_dat is {row.count_persons}'
    
if __name__ == '__main__':
    procedure_count_rows()
    procedure_count_persons_for_n_last_date(3)

