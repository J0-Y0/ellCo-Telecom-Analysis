# ellCo-Telecom-Analysis

## Overview
This repository contains an analysis of TellCo, a mobile service provider in the Republic of Pefkakia. The project explores customer data to identify growth opportunities and provides insights through a web-based dashboard and a detailed report. The analysis aims to guide an investment decision on whether to buy or sell the company.

## Main Project Structure

```bash
ellCo-Telecom-Analysis/
├── .gitignore                     # Git ignore file
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── notebooks/
│   ├── __init__.py
│   ├── user_overview_analysis.ipynb     # user over view analysis notebook
│   └── README.md                        # Additional Insights and finding  on the EDA Performed
├── scripts/
│   ├── graph.py.py               # utility for optimizing   plotting functions
│   ├── analyzer.py               # Utility for for analyzing the data 
│   ├── db_connection.py          # database connection and queries 
```

## Getting Started

### Prerequisites

- Ensure you have Python 3.x installed on your system.
- PostgreSQL database with access credentials for TellCo data.

### Installation
1. **Clone the repository:**

   ```bash
   git clone https://github.com/J0-Y0/ellCo-Telecom-Analysis.git
   cd ellCo-Telecom-Analysis
2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Configure Database Connection:**
    - Create a `.env` file in the root directory and add your PostgreSQL database credentials:

    ```bash
        DATABASE_HOST=your_database_host
        DATABASE_PORT=5432
        DATABASE_NAME=your_database_name
        DATABASE_USER=your_database_user
        DATABASE_PASSWORD=your_database_password
    ```

    - Ensure that `.env` is listed in your .gitignore to avoid committing it to version control.
    - Ensure `db_connection.py` is updated with your PostgreSQL database credentials. This script manages the connection to the database and executes queries to retrieve TellCo's data.



4. **Get the EDA  and my findings  under the `notebooks/` directory:**
    ``` bash
        stock_market_data_analysis/
        ├── notebooks/
        │   ├── user_overview_analysis.ipynb    # user over view technical analysis 
        │   └── README.md                      # Additional Insights and findings
# Data Fields Summary


## Fields and Descriptions

| **Field**                           | **Description**                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| `bearer id`                         | xDR session identifier.                                                                          |
| `Dur. (ms)`                         | Total Duration of the xDR (in milliseconds).                                                     |
| `Start`                             | Start time of the xDR (first frame timestamp).                                                   |
| `Start ms`                          | Milliseconds offset of start time for the xDR (first frame timestamp).                           |
| `End`                               | End time of the xDR (last frame timestamp).                                                       |
| `End ms`                            | Milliseconds offset of end time of the xDR (last frame timestamp).                               |
| `Dur. (s)`                          | Total Duration of the xDR (in seconds).                                                           |
| `IMSI`                              | International Mobile Subscriber Identity.                                                         |
| `MSISDN/Number`                     | MS International PSTN/ISDN Number of mobile - customer number.                                  |
| `IMEI`                              | International Mobile Equipment Identity.                                                         |
| `Last Location Name`               | User location call name (2G/3G/4G) at the end of the bearer.                                     |
| `Avg RTT DL (ms)`                   | Average Round Trip Time measurement Downlink direction (milliseconds).                           |
| `Avg RTT UL (ms)`                   | Average Round Trip Time measurement Uplink direction (milliseconds).                             |
| `Avg Bearer TP DL (kbps)`            | Average Bearer Throughput for Downlink (kbps) - based on BDR duration.                           |
| `Avg Bearer TP UL (kbps)`            | Average Bearer Throughput for Uplink (kbps) - based on BDR duration.                             |
| `TCP DL Retrans. Vol (Bytes)`       | TCP volume of Downlink packets detected as retransmitted (bytes).                                |
| `TCP UL Retrans. Vol (Bytes)`       | TCP volume of Uplink packets detected as retransmitted (bytes).                                  |
| `DL TP < 50 Kbps (%)`               | Duration ratio when Bearer Downlink Throughput < 50 Kbps.                                         |
| `50 Kbps < DL TP < 250 Kbps (%)`    | Duration ratio when Bearer Downlink Throughput is between 50 Kbps and 250 Kbps.                  |
| `250 Kbps < DL TP < 1 Mbps (%)`     | Duration ratio when Bearer Downlink Throughput is between 250 Kbps and 1 Mbps.                   |
| `DL TP > 1 Mbps (%)`                | Duration ratio when Bearer Downlink Throughput > 1 Mbps.                                         |
| `UL TP < 10 Kbps (%)`               | Duration ratio when Bearer Uplink Throughput < 10 Kbps.                                           |
| `10 Kbps < UL TP < 50 Kbps (%)`     | Duration ratio when Bearer Uplink Throughput is between 10 Kbps and 50 Kbps.                    |
| `50 Kbps < UL TP < 300 Kbps (%)`    | Duration ratio when Bearer Uplink Throughput is between 50 Kbps and 300 Kbps.                   |
| `UL TP > 300 Kbps (%)`              | Duration ratio when Bearer Uplink Throughput > 300 Kbps.                                         |
| `HTTP DL (Bytes)`                   | HTTP data volume (in Bytes) received by the MS during this session.                              |
| `HTTP UL (Bytes)`                   | HTTP data volume (in Bytes) sent by the MS during this session.                                  |
| `Activity Duration DL (ms)`         | Activity Duration for downlink (in milliseconds) excluding periods of inactivity > 500 ms.        |
| `Activity Duration UL (ms)`         | Activity Duration for uplink (in milliseconds) excluding periods of inactivity > 500 ms.          |
| `Dur. (ms).1`                       | Total Duration of the xDR (in milliseconds).                                                     |
| `Handset Manufacturer`              | Handset manufacturer.                                                                            |
| `Handset Type`                      | Handset type of the mobile device.                                                                |
| `Nb of sec with 125000B < Vol DL`   | Number of seconds with IP Volume DL > 125,000 Bytes.                                             |
| `Nb of sec with 1250B < Vol UL < 6250B` | Number of seconds with IP Volume UL between 1,250 Bytes and 6,250 Bytes.                        |
| `Nb of sec with 31250B < Vol DL < 125000B` | Number of seconds with IP Volume DL between 31,250 Bytes and 125,000 Bytes.                    |
| `Nb of sec with 37500B < Vol UL`    | Number of seconds with IP Volume UL > 37,500 Bytes.                                             |
| `Nb of sec with 6250B < Vol DL < 31250B` | Number of seconds with IP Volume DL between 6,250 Bytes and 31,250 Bytes.                     |
| `Nb of sec with 6250B < Vol UL < 37500B` | Number of seconds with IP Volume UL between 6,250 Bytes and 37,500 Bytes.                     |
| `Nb of sec with Vol DL < 6250B`     | Number of seconds with IP Volume DL < 6,250 Bytes.                                               |
| `Nb of sec with Vol UL < 1250B`     | Number of seconds with IP Volume UL < 1,250 Bytes.                                               |
| `Social Media DL (Bytes)`           | Social Media data volume (in Bytes) received by the MS during this session.                      |
| `Social Media UL (Bytes)`           | Social Media data volume (in Bytes) sent by the MS during this session.                          |
| `YouTube DL (Bytes)`                | YouTube data volume (in Bytes) received by the MS during this session.                           |
| `YouTube UL (Bytes)`                | YouTube data volume (in Bytes) sent by the MS during this session.                               |
| `Netflix DL (Bytes)`                | Netflix data volume (in Bytes) received by the MS during this session.                           |
| `Netflix UL (Bytes)`                | Netflix data volume (in Bytes) sent by the MS during this session.                               |
| `Google DL (Bytes)`                 | Google data volume (in Bytes) received by the MS during this session.                            |
| `Google UL (Bytes)`                 | Google data volume (in Bytes) sent by the MS during this session.                                |
| `Email DL (Bytes)`                  | Email data volume (in Bytes) received by the MS during this session.                             |
| `Email UL (Bytes)`                  | Email data volume (in Bytes) sent by the MS during this session.                                 |
| `Gaming DL (Bytes)`                 | Gaming data volume (in Bytes) received by the MS during this session.                            |
| `Gaming UL (Bytes)`                 | Gaming data volume (in Bytes) sent by the MS during this session.                                |
| `Other DL`                          | Other data volume (in Bytes) received by the MS during this session.                             |
| `Other UL`                          | Other data volume (in Bytes) sent by the MS during this session.                                 |
| `Total DL (Bytes)`                  | Total data volume (in Bytes) received by the MS during this session (IP layer + overhead).       |
| `Total UL (Bytes)`                  | Total data volume (in Bytes) sent by the MS during this session (IP layer + overhead).           |


## License
This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.