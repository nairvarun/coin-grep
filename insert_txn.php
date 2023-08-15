<?php
function insert_into_db($val) {
    include('dbcoonnector.php');
    $sql = "INSERT INTO  transaction (transaction) VALUES ('$val')";

    if (!mysqli_query($conn, $sql)) {
        echo "Error: " . mysqli_error($conn);
    }
}


if (isset($_GET['val'])) {
    $val = $_GET['val'];
    insert_into_db($val);
    // $result = insert_into_db($val);
    echo 'ok';
}
?>
