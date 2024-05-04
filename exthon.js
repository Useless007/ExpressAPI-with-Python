const express = require("express");
const app = express();
const port = 4000;
const { exec } = require("child_process");

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post("/api/create-user", (req, res) => {
  // console.log(req.body);
  exec(`python3.12 ./python/create_data.py ${req.body.name}`, (error, stdout) => {

    if (error) {
      res.status(400).send(`เกิดข้อผิดพลาด: ${error}`);
      return;
    }

    res.status(200).send(`ผลลัพธ์: ${stdout}`);
  });
});

// แสกนใบหน้าและเก็บdata - ชื่อ&ข้อมูลเวลาแสกน
app.get("/api/scan-user", (req, res) => {
  exec("python3.12 ./python/face_Detection.py", (error, stdout) => {
    if (error) {
      console.error(`เกิดข้อผิดพลาด: ${error}`);
      return;
    }
    res.status(200).send(`ผลลัพธ์: ${stdout}`);
  });
});

// แสกนใบหน้า
app.get("/api/recog-user", (req, res) => {
  exec("python3.12 ./python/face_recognize.py", (error, stdout) => {
    if (error) {
      console.error(`เกิดข้อผิดพลาด: ${error}`);
      return;
    }
    res.status(200).send(`ผลลัพธ์: ${stdout}`);
  });
});

// นำข้อมูลจากcsvเข้าสู่database
app.get("/api/csv-db", (req, res) => {
  exec("python3.12 ./python/CSV_to_pstgsql.py", (error, stdout) => {
    if (error) {
      console.error(`เกิดข้อผิดพลาด: ${error}`);
      return;
    }
    res.status(200).send(`ผลลัพธ์: ${stdout}`);
  });
});



app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
