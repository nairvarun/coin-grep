<!DOCTYPE html>
<html>
<head>
    <title>Blockchain Query Results</title>
    <link rel="stylesheet" type="text/css" href="./style.css">
</head>
<body>
    <div id="res_header"><em><a href="index.php">coin-grep</a></em></div>
    <!-- <div id="main">
        <input type="search" id="search" name="search" placeholder="addr/tnx">
        <button type="submit" id="submit">🔍</button>
    </div> -->
    <br><br>
    <div id="res_qry">
        ₿ <span><?php echo $_GET['search']; ?></span>
    </div>

    <div id="res_result">
        <?php
        require 'helpers.php';

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
</body>
</html>
