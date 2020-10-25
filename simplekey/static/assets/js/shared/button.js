//$(function(){
//        $("#bt1").click(function(){
//            $(this).attr("disabled", "disabled");
//            $("#bt2").removeAttr("disabled");
//        });
//
//        $("#bt2").click(function () {
//            $(this).attr("disabled", "disabled");
//            $("#bt1").removeAttr("disabled");
//        });
//    });

                          {% if i[25] == 'False' %}
                            <td>
                              <a href="/admin_buy_active/{{i[0]}}" class="btn btn-success btn-sm" style="color: white; width:100% ">Activate</a>
                            </td>
                          {% else %}
                            <td>
                              <a href="/admin_buy_deactive/{{i[0]}}" class="btn btn-danger btn-sm" style="color: white; width:100% " >Deactivate</a>
                            </td>
                          {% endif %}