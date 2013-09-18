# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>Add a new file</h1>

<form action="${request.route_path('new')}" method="post" enctype="multipart/form-data">
  <input type="text" maxlength="100" name="fdescr">
  </br>
  </br>
  <label for="txt">txt</label>
  <input id='files' type="file" name="fname" value=""/>
  </br>
  </br>
  <input type="submit" name="add" value="ADD" class="button">
</form>
