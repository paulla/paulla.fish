# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>
<form action="${request.route_path('new')}" method="post" enctype="multipart/form-data">
  <input id='files' type="file" name="fname" value=""/>
    </br>
  </br>
  <input class="inDescr" type="text" placeholder="Enter your description here" maxLength="100" name="fdescr">
  </br>
  </br>
<input type="submit" name="add" value="Submit" class="btn">
</form>
