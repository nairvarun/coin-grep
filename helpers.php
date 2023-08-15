<?php
function query() {
    $qry = $_POST['search'];

    if (strlen($qry) === 64) {
        query_txn($qry);
    } else {
        query_addr($qry);
    }
}

function query_addr($addr) {
    include('db_connection.php');
    $url = "https://api.blockcypher.com/v1/btc/main/addrs/$addr";
    $response = makeRequest($url);
    $res = json_decode($response, true);

    echo '<br><br>';

    echo '<table class="res_result">';
    echo '<tr><td>Received <br><br><span class="res_bnum">' . $res['total_received'] . ' SATS</span></td>';
    echo '<td>Sent <br><br><span class="res_bnum">' . $res['total_sent'] . ' SATS</span></td>';
    echo '<td>Balance <br><br><span class="res_bnum">' . $res['balance'] . ' SATS</span></td>';
    echo '<td>Transactions <br><br><span class="res_bnum">' . $res['n_tx'] . '</span></td>';
    echo '</table>';

    echo '<br><br>';

    echo '<table class="res_extra_result">';
    echo '<tr>';
    echo '<td>Total Received</td>';
    echo '<td>' . $res['total_received'] * 0.00000001 . ' BTC</td>';
    echo '</tr>';
    echo '<tr>';
    echo '<td>Total Sent</td>';
    echo '<td>' . $res['total_sent'] * 0.00000001 . ' BTC</td>';
    echo '</tr>';
    echo '<tr>';
    echo '<td>Balance</td>';
    echo '<td>' . $res['balance'] * 0.00000001 . ' BTC</td>';
    echo '</tr>';
    echo '<tr>';
    echo '<td>Unconfirmed Balance</td>';
    echo '<td>' . $res['unconfirmed_balance'] . '</td>';
    echo '</tr>';
    echo '<tr>';
    echo '<td>Total Transactions</td>';
    echo '<td>' . $res['n_tx'] . '</td>';
    echo '</tr>';
    echo '<td>Unconfirmed Transactions</td>';
    echo '<td>' . $res['unconfirmed_n_tx'] . '</td>';
    echo '</tr>';
    echo '<tr>';
    echo '<td class="res_top">Transactions</td>';
    echo '<td>';
    foreach ($res['txrefs'] as $tx) {
        $curr_tx=$tx['tx_hash'];
        $sql1 = "SELECT * FROM transaction WHERE transaction = '$curr_tx'";
        $result = $conn->query($sql1);
        if ($result->num_rows > 0) {
            $exists = true;
        } else {
            $exists = false;
        }

        if ($exists) {
            echo '<input type="checkbox" onchange="handle_txn(this.checked, `' . $curr_tx . '`)" checked> <a class="flag" href="results.php?search=' . $curr_tx . '">' . $curr_tx . '</a><br><br>';
        } else {
            echo '<input type="checkbox" onchange="handle_txn(this.checked, `' . $curr_tx . '`)"> <a href="results.php?search=' . $curr_tx . '">' . $curr_tx . '</a><br><br>';
        }
    }
    echo '</td>';
    echo '</tr>';
    echo '</table>';
}

function query_txn($txn_id) {
    include('db_connection.php');
    $url = "https://api.blockcypher.com/v1/btc/main/txs/$txn_id";
    $response = makeRequest($url);
    $res = json_decode($response, true);

    echo '<br><br>';

    echo '<table class="res_result">';
    echo '<tr><td>Amount Transacted <br><br><span class="res_bnum">' . $res['total'] . '</span></td>';
    echo '<td>Fees <br><br><span class="res_bnum">' . $res['fees'] . '</span></td>';
    echo '<td>Block Height <br><br><span class="res_bnum">' . $res['block_height'] . '</span></td>';
    echo '<td>Confirmations <br><br><span class="res_bnum">' . $res['confirmations'] . '</span></td></tr>';
    echo '</table>';

    echo '<br><br>';

    echo '<table class="res_extra_result">';
    echo '<tr>';
    echo '<td>Block Hash</td>';
    echo '<td>' . $res['block_hash'] . '</td>';
    echo '</tr>';
    echo '<tr>';
    echo '<td>Block Height</td>';
    echo '<td>' . $res['block_height'] . '</td>';
    echo '</tr>';
    echo '<tr>';
    echo '<td>Transaction Index</td>';
    echo '<td>' . $res['block_index'] . '</td>';
    echo '</tr>';
    echo '<tr>';
    echo '<td>Size</td>';
    echo '<td>' . $res['size'] . '</td>';
    echo '</tr>';
    echo '<tr>';
    echo '<td>Preference</td>';
    echo '<td>' . $res['preference'] . '</td>';
    echo '</tr>';
    echo '<tr>';
    echo '<td>Confidence</td>';
    echo '<td>' . $res['confidence'] . '</td>';
    echo '</tr>';
    echo '<tr>';
    echo '<td class="res_top">Sent To</td>';
    echo '<td>';
    foreach ($res['addresses'] as $ad) {
        $sql1 = "SELECT * FROM Adress WHERE adress = '$ad' ";
        $result = $conn->query($sql1);
        if ($result->num_rows > 0) {
            $exists = true;
        } else {
            $exists = false;
        }

        if ($exists) {
            echo '<input type="checkbox" onchange="handle_addr(this.checked, `' . $ad . '`)" checked> <a class="flag" href="results.php?search=' . $ad . '">' . $ad . '</a><br><br>';
        } else {
            echo '<input type="checkbox" onchange="handle_addr(this.checked, `' . $ad . '`)"> <a href="results.php?search=' . $ad . '">' . $ad . '</a><br><br>';
        }
    }
    echo '</td>';
    echo '</tr>';
    echo '</table>';
}

function makeRequest($url) {
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    curl_close($ch);
    return $response;
}

function del_addr_from_db($val) {
    include('db_connection.php');
    $sql = "DELETE FROM Adress WHERE adress = '$val'";

    if (!mysqli_query($conn, $sql)) {
        echo "Error: " . mysqli_error($conn);
    }
}

function insert_addr_into_db($val) {
    include('db_connection.php');
    $sql = "INSERT INTO  Adress (adress) VALUES ('$val')";

    if (!mysqli_query($conn, $sql)) {
        echo "Error: " . mysqli_error($conn);
    }
}

function del_txn_from_db($val) {
    include('db_connection.php');
    $sql = "DELETE FROM transaction WHERE transaction = '$val'";

    if (!mysqli_query($conn, $sql)) {
        echo "Error: " . mysqli_error($conn);
    }
}

function insert_txn_into_db($val) {
    include('db_connection.php');
    $sql = "INSERT INTO  transaction (transaction) VALUES ('$val')";

    if (!mysqli_query($conn, $sql)) {
        echo "Error: " . mysqli_error($conn);
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    query();
}
?>
