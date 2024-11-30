 <?php
 // Отримати дані з запиту
 $data = json_decode(file_get_contents("php://input"), true);

 if ($data) {
     // Зберегти дані у файл tabs.json
     file_put_contents('tabs.json', json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));
     echo json_encode(["status" => "success", "message" => "Tabs saved successfully"]);
 } else {
     echo json_encode(["status" => "error", "message" => "No data received"]);
 }
 ?>
