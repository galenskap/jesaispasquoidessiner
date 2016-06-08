<p>Objets:</p>
<table border="1">
%for row in objets:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>

<p>Situations:</p>
<table border="1">
%for row in situations:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>
