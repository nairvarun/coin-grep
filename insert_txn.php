<?php
require_once('helpers.php');

if (isset($_GET['val'])) {
    $val = $_GET['val'];
    insert_txn_into_db($val);
    // $result = insert_into_db($val);
    echo 'insert_txn_into_db(): ok';
}
?>
