<?php
require_once('helpers.php');

if (isset($_GET['val'])) {
    $val = $_GET['val'];
    del_txn_from_db($val);
    // $result = insert_into_db($val);
    echo 'del_txn_from_db(): ok';
}
?>