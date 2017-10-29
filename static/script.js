function my_func(temp) {
    var element = document.getElementById("div1");
    var head = document.createElement("H1");
    var head_node = document.createTextNode("Even Fibonacci Number Series");
    head.appendChild(head_node);
    element.appendChild(head);

    for (var i = 0; i < temp.length; i++){
            if ((temp[i] % 2) == 0) {
                console.log(temp[i])
                var para = document.createElement("P");
                var node = document.createTextNode(temp[i]);
                para.appendChild(node);
                element.appendChild(para);

            }
        }
   }
