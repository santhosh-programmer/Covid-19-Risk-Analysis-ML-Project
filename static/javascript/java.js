function fn(x,y,z,s) {
    if(s=="y")
    {
        if(document.getElementById(y).classList.contains("no"))
        {
            document.getElementById(y).classList.remove("no");
        }
        document.getElementById(x).classList.add("yes");
        document.getElementById(z).setAttribute("value","1");
    }
    else
    {
        if(document.getElementById(y).classList.contains("yes"))
        {
            document.getElementById(y).classList.remove("yes");
        }
        document.getElementById(x).classList.add("no");
        document.getElementById(z).setAttribute("value","2");

    }
}

