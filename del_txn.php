<?php
function del_from_db($val) {
    include('dbcoonnector.php');
    $sql = "DELETE FROM transaction WHERE transaction = '$val'";

    if (!mysqli_query($conn, $sql)) {
        echo "Error: " . mysqli_error($conn);
    }
}


if (isset($_GET['val'])) {
    $val = $_GET['val'];
    del_from_db($val);
    // $result = insert_into_db($val);
    echo 'ok';
}
?>
