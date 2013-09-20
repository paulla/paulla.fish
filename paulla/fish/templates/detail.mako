# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>
  <figure>
  ${file_data[4]}
  <a href="${request.route_path('dl', id=file_data[0], fname=file_data[4])}">
  <img src="${request.route_path('dl', id=file_data[0], fname=file_data[4])}" alt="${file_data[4]}"></img>
  </a>
  <figcaption>
  <span class="name">
  Description de l'image : <br>${file_data[1]}
  </span>
  </figcaption>
</figure>
  <li class="last">
    <a href="${request.route_path('list')}">Back to the future</a>
  </li>
