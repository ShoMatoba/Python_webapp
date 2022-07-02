function change_table(){
    table_obj = document.getElementById('table_id');
    if(flag){
        table_obj.style.backgroundColor = "red";
        flag = false;
    }else{
        table_obj.style.backgroundColor  = "";
        flag = true;
    }
    
}
let flag = true;