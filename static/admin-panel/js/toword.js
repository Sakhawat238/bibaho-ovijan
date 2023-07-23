    
     
    
    var taka = "";
    var paisa = "";
    
    function trimFB(stringToTrim) 
    {
	    return stringToTrim.replace(/^\s+|\s+$/g,"");
    }

    function toword(d)
    {
        var temp=new Array();
        temp=ParseDoubletoText(d);
        var money = taka + " Taka";

        if (paisa!= "")
            money += " " + paisa + " Paisa";
        money = trim(money);
        return trimFB(money);
    }
    
   function trim(s) 
   { 
    var l=0; var r=s.length -1; 
        while(l < s.length && s[l] == ' ') 
        {     l++; } 
        while(r > l && s[r] == ' ') 
        {     r-=1;     } 
        return s.substring(l, r+1); 
   }

    function GetDigitstr(digit)
    {
        var str = "";
        if (digit < 20)
        {
            switch (digit)
            {
                case 1:
                    str = "One";
                    break;
                case 2:
                    str = "Two";
                    break;
                case 3:
                    str = "Three";
                    break;
                case 4:
                    str = "Four";
                    break;
                case 5:
                    str = "Five";
                    break;
                case 6:
                    str = "Six";
                    break;
                case 7:
                    str = "Seven";
                    break;
                case 8:
                    str = "Eight";
                    break;
                case 9:
                    str = "Nine";
                    break;
                case 10:
                    str = "Ten";
                    break;
                case 11:
                    str = "Eleven";
                    break;
                case 12:
                    str = "Twelve";
                    break;
                case 13:
                    str = "Thirteen";
                    break;
                case 14:
                    str = "Fourteen";
                    break;
                case 15:
                    str = "Fifteen";
                    break;
                case 16:
                    str = "Sixteen";
                    break;
                case 17:
                    str = "Seventeen";
                    break;
                case 18:
                    str = "Eighteen";
                    break;
                case 19:
                    str = "Nineteen";
                    break;
            }
        }
        else
        {
            var decimaldigit = Math.floor(digit / 10);
            str += Getdecimalstr(decimaldigit) + " ";
            var restdigit = digit - decimaldigit * 10;
            if (restdigit > 0)
            {
                str += GetDigitstr(restdigit);
            }
        }
        return str;
    }
    
    function Getdecimalstr(decimaldigit)
    {
        var str = "";
        switch (decimaldigit)
        {
            case 2:
                str = "Twenty";
                break;
            case 3:
                str = "Thirty";
                break;
            case 4:
                str = "Fourty";
                break;
            case 5:
                str = "Fifty";
                break;
            case 6:
                str = "Sixty";
                break;
            case 7:
                str = "Seventy";
                break;
            case 8:
                str = "Eighty";
                break;
            case 9:
                str = "Ninety";
                break;
        }
        return str;
    }
    
    function ParseDoubletoText(amount)
    {
        var Am = amount;
        var str=""
        var paisastr="";
        var croredigit = Am / 10000000;
        if (croredigit > 0)
        {
            var temp=ParseDoubletoText(croredigit);
            str += " " + taka;
        }
        var crore = Math.floor(croredigit);

        if (crore > 0)
        {
            str += " Crore ";
        }
        Am -= crore * 10000000;

        var lacdigit = Math.floor(Am / 100000);
        str += GetDigitstr(lacdigit);
        if (lacdigit > 0)
        {
            str += " Lac ";
        }
        Am -= lacdigit * 100000;
        var thousanddigit = Math.floor(Am / 1000);
        str += GetDigitstr(thousanddigit);
        if (thousanddigit > 0)
        {
            str += " Thousand ";
        }
        Am -= thousanddigit * 1000;

        var hundreddigit = Math.floor(Am / 100);
        str += GetDigitstr(hundreddigit);
        if (hundreddigit > 0)
        {
            str += " Hundred ";
        }
        Am -= hundreddigit * 100;

        var rest = Math.floor(Am);
        str += GetDigitstr(rest);

        Am -= rest;
        if (Am > 0)
        {

            var paisa1 = Math.floor(Am * 100);
            paisastr = GetDigitstr(paisa1);

        }
        paisa=paisastr;
        taka = str;
        
        var arr=new Array();
        
        return arr;
    }

