import csv

# Open the CSV file
with open('data.csv', newline='') as csvfile:
    # Create a CSV reader
    reader = csv.reader(csvfile)
    
    # Loop through each row in the CSV file
    for row in reader:
        # Create an array from the row
        data = list(row)
        
        # Build the SQL query
        query = "INSERT INTO dataset (id, instrument_name, localDate, local_time, co, o3, no2, so2, no_, voc, pm2p5, pm10, rh, pressure, sensorTemp, heaterTemp, internalTemp, timeRec, UTCdate, UTCtime, alarms) VALUES ({}, '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}', '{}', '{}', '{}');".format(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4],
            data[5],
            data[6],
            data[7],
            data[8],
            data[9],
            data[10],
            data[11],
            data[12],
            data[13],
            data[14],
            data[15],
            data[16],
            data[17],
            data[18],
            data[19],
            data[20]
        )
        
        # Write the SQL query to a file
        with open('queries.sql', 'a') as f:
            f.write(query + '\n')
