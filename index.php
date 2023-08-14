<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./style.css">
    <title>coin-grep</title>
</head>
<body>
    <div id="idx_logo"><em><a href="index.php">coin-grep</a></em></div>
    <!-- <div id="idx_logo"><em>coin-grep</em></div> -->
    <div id="idx_main">
        <span id="idx_slogan">Search the Bitcoin Blockchain</span>
        <form action="./results.php" method="get">
            <br>
            <input type="search" id="idx_search" name="search" autofocus="" placeholder="Example: 16Fg2yjwrbtC6fZp61EV9mNVKmwCzGasw5" required>
            <button type="submit" id="idx_submit">🔍</button>
            <br><br>
            <em>Enter an
                <a href="javascript:void(0);" onclick="fill_addr()">address</a> or a
                <a href="javascript:void(0);" onclick="fill_txn()">transaction hash</a>
        </form>
    </div>

    <script src="./script.js"></script>
</body>
</html>
