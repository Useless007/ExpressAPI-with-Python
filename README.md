you need to change the pstgsql setting on 

CSV_to_pstgsql.py

and you need to create face data before using face_detection and face_recognize
by this API route
```
POST http://localhost:4000/api/create-user
```
you need to send request payload with
```
{
    "name":"yourname"
}
```

by using face detection and it will put the timestamp and your name on 
data_with_timestamp.csv
```
GET http://localhost:4000/api/scan-user
```

by using face recognize it will recognize and it not autometically escape the python you need to press the ESC button to quit
```
GET http://localhost:4000/api/recog-user
```

you can import csv to your postgresdb by this api route
```
GET http://localhost:4000/api/csv-db
```
