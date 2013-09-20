# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>
% for task in tasks:
  <li class="download">
    <span class="filename">${task['fname']}</span>
    <a href="detail/${task['id']}/${task['fname']}">detail</a><a href="${request.route_path('close', id=task['id'])}">close</a>
    <a href="dl/${task['id']}/${task['fname']}"></a>
  </li>
% endfor
