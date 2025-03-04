# Uber ETL Analytics

## Overview
This project aims to perform data analytics on Uber data using modern data engineering tools and technologies. The workflow includes data extraction, transformation, and loading (ETL) processes, leveraging Google Cloud Platform (GCP) services, Python, and Mage—AI data pipeline tool. The ultimate goal is to derive meaningful insights from Uber trip records by processing and analyzing the data efficiently.

## Features
- **Data Ingestion**: Utilize GCP Storage to securely store raw data on Uber trips.
- **Data Processing**: Implement data transformation, and cleaning using Python and Mage AI to ensure quality and consistency.
- **Data Warehousing**: Load the processed data into BigQuery for scalable and efficient querying.
- **Data Visualization**: Create interactive dashboards and reports using Looker Studio to visualize key metrics and trends.

## Usage
1. **Set Up GCP Services**:
    - Create a GCP project and enable the necessary APIs for Storage, Compute Engine, and BigQuery.
    - Set up a Compute Instance to run the ETL processes.
2. **Install Required Tools**:
    - On the Compute Instance, install Python and pip.
    - Install Mage AI for orchestrating data pipelines.
    - Install any necessary Python libraries such as Pandas and Google Cloud libraries.
3. **Configure Mage Pipeline**:
    - Define the ETL pipeline using Mage-AI to extract data from GCP Storage and transform it.
4. **Execute the Pipeline**:
    - Run the Mage pipeline to process the Uber data and load it into BigQuery.
5. **Visualize Data**:
    - Connect Looker Studio to BigQuery and create dashboards to visualize the analytics.

## Prerequisites
- **Python Environment**: Python installed on the Compute Instance along with pip.
- **Python Libraries**: Pandas and Google Cloud libraries installed for data processing and interaction with GCP services.
- **Google Cloud Platform Account**: Access to GCP services like Storage, Compute Engine, and BigQuery.
- **Mage Installation**: Mage data pipeline tool installed for orchestrating ETL processes.

## Input
The project utilizes the TLC Trip Record Data, which includes yellow and green taxi trip records.\
These records capture:\
    - Pick-up and drop-off dates/times
    - Pick-up and drop-off locations
    - Trip distances
    - Itemized fares
    - Rate types
    - Payment types
    - Driver-reported passenger counts
The specific dataset used in this project can be found here:\
More information about the dataset is available on the NYC Taxi and Limousine Commission website.

## Output
The processed data is stored in BigQuery for efficient querying and analysis. Key outputs include:

    - **Analytics Table**: A consolidated table in BigQuery that combines various dimensions such as trip details, passenger counts, rates, locations, and payment types.
    - **Visualizations**: Interactive dashboards and reports created in Looker Studio, providing insights into trip patterns, fare distributions, and other relevant metrics.
