function fill_addr() {
    document.querySelector('#idx_search').value = 'bc1qae22e0z0prjzk46f6mphf29uvc723yyvc3jmm2'
}

function fill_txn() {
    document.querySelector('#idx_search').value = '9b60eb6bdf8dd0520d18320865b044dae8edf444683de9c1e4c02b15e949a42c'
}


// document.getElementById('searchbar').onkeydown = function (e) {
//     if (e.key == 'Enter') {
//         location.href = `items/${document.getElementById('searchbar').value}`
//     }
// };



// // https://api.blockcypher.com/v1/btc/main/txs/9b60eb6bdf8dd0520d18320865b044dae8edf444683de9c1e4c02b15e949a42c
// // 9b60eb6bdf8dd0520d18320865b044dae8edf444683de9c1e4c02b15e949a42c
// // bc1qae22e0z0prjzk46f6mphf29uvc723yyvc3jmm2

// function query() {
//     qry = document.querySelector('#search').value
//     if (qry.length === 64) {
//         query_txn(qry)
//     } else {
//         query_addr(qry)
//     }
// }

// function query_addr(addr) {
//     var xhttp = new XMLHttpRequest()
//     xhttp.onreadystatechange = function() {
//         if (this.readyState == 4 && this.status == 200) {
//             let res = JSON.parse(this.responseText)
//             document.querySelector('#result').innerHTML = `
//                 ${res.address}<br>
//                 ${res.total_sent}<br>
//                 ${res.total_total_received}<br>
//                 ${res.balance}<br>`
//         }
//     }
//     xhttp.open("GET", "https://api.blockcypher.com/v1/btc/main/addrs/" + addr, true)
//     xhttp.send()
// }

// function query_txn(txn_id) {
//     var xhttp = new XMLHttpRequest()
//     xhttp.onreadystatechange = function() {
//         if (this.readyState == 4 && this.status == 200) {
//             res = JSON.parse(this.responseText)
//             document.querySelector('#result').innerHTML = `
//             ${res.block_height}<br>
//             ${res.total}<br>
//             ${res.fees}<br>
//             ${res.addresses}<br>
//             `

//         }
//     }
//     xhttp.open("GET", "https://api.blockcypher.com/v1/btc/main/txs/" + txn_id, true)
//     xhttp.send()
// }

// // function loadDoc() {
// //     var xhttp = new XMLHttpRequest();
// //     xhttp.onreadystatechange = function() {
// //       if (this.readyState == 4 && this.status == 200) {
// //        console.log(this.responseText);
// //       }
// //     };
// //     xhttp.open("GET", "https://api.blockcypher.com/v1/btc/main/txs/9b60eb6bdf8dd0520d18320865b044dae8edf444683de9c1e4c02b15e949a42c", true);
// //     xhttp.send();
// //   }
