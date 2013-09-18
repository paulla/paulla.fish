# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>File's Sharing List</h1>
<ul id="tasks">
% if tasks:
  % for task in tasks:
  <li>
    <span class="name"><a href="dl/${task['id']}/${task['fname']}">${task['fname']}</a> : ${task['fdescr']}</span>
    <span class="actions">[ <a href="detail/${task['id']}/${task['fname']}">detail</a> ][ <a href="${request.route_path('close', id=task['id'])}">close</a> ]</span>
  </li>
  % endfor
% else:
  <li>There are no file</li>
% endif
  <li class="last">
    <a href="${request.route_path('new')}">Add a new file</a>
  </li>
</ul>
