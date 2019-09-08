% rebase("osnova")

% if isinstance(rezultat, float):
    <div align="center">
    <h1>{{ rezultat }}</h1>
    </div>

% else:
  <div align="center">
  <h1>
  <table>
%   for vrstica in rezultat:
      <tr>
      <td>{{vrstica}}</td>
      </tr>
% end
  </table>
  </h1>
  </div>

<div align="right">
  <a href="/" class="btn btn-outline-secondary" role="button" aria-pressed="true">Domov</a>
</div>
