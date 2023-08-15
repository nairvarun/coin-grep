<!DOCTYPE html>
<html>
<head>
    <title>Blockchain Query Results</title>
    <link rel="stylesheet" type="text/css" href="./style.css">
</head>
<body>
    <div id="res_header"><em><a href="index.php">coin-grep</a></em></div>
    <br><br>
    <div id="res_qry">
        <?php
            require_once('db_connection.php');
            $curr = $_GET['search'];
            $sql1 = "SELECT * FROM transaction WHERE transaction = '$curr'";
            $result = $conn->query($sql1);
            if ($result->num_rows > 0) {
                $exists = true;
            } else {
                $exists = false;
            }

            if ($exists) {
                echo '<input type="checkbox" onchange="handle_txn(this.checked, `' . $curr . '`)" checked> <span class="flag">'.$curr.'</span>';
            } else {
                echo '<input type="checkbox" onchange="handle_txn(this.checked, `' . $curr . '`)"> <span>'.$curr.'</span>';
            }
        ?>
    </div>

    <div id="res_result">
        <?php
        require_once('helpers.php');

        if (isset($_GET['search'])) {
            $search = $_GET['search'];
            if (strlen($search) === 64) {
                query_txn($search);
            } else {
                query_addr($search);
            }
        }
        ?>
    </div>
    <script src="./script.js"></script>
    <script>
        function handle_addr(checked, val) {
            if (checked) {
                var xhr = new XMLHttpRequest();
                xhr.open("GET", "insert_addr.php?val=" + val, true);
                xhr.onreadystatechange = function () {
                    if (xhr.readyState === XMLHttpRequest.DONE) {
                        if (xhr.status === 200) {
                            console.log(xhr.responseText); // Response from PHP
                        }
                    }
                };
                xhr.send();
            } else {
                var xhr = new XMLHttpRequest();
                xhr.open("GET", "del_addr.php?val=" + val, true);
                xhr.onreadystatechange = function () {
                    if (xhr.readyState === XMLHttpRequest.DONE) {
                        if (xhr.status === 200) {
                            console.log(xhr.responseText); // Response from PHP
                        }
                    }
                };
                xhr.send();
            }
        }

        function handle_txn(checked, val) {
            if (checked) {
                var xhr = new XMLHttpRequest();
                xhr.open("GET", "insert_txn.php?val=" + val, true);
                xhr.onreadystatechange = function () {
                    if (xhr.readyState === XMLHttpRequest.DONE) {
                        if (xhr.status === 200) {
                            console.log(xhr.responseText); // Response from PHP
                        }
                    }
                };
                xhr.send();
            } else {
                var xhr = new XMLHttpRequest();
                xhr.open("GET", "del_txn.php?val=" + val, true);
                xhr.onreadystatechange = function () {
                    if (xhr.readyState === XMLHttpRequest.DONE) {
                        if (xhr.status === 200) {
                            console.log(xhr.responseText); // Response from PHP
                        }
                    }
                };
                xhr.send();
            }

        }
    </script>

</body>
</html>
