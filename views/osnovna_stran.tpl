% rebase("osnova")

<div class="container">

<div class="mx-auto" style="width: 300px;">
  <h1>Matrikarko!</h1>
  </div>

<div class="btn-group-vertical" role="group" aria-label="Button group with nested dropdown">
  <a href="/normalnost" class="btn btn-secondary">seštej</a>       
  <button type="button" class="btn btn-secondary">odštej</button> 
  <button type="button" class="btn btn-secondary">pomnoži</button> 
  <button type="button" class="btn btn-secondary">sledi</button> 
  <button type="button" class="btn btn-secondary">transponiraj</button> 
  <button type="button" class="btn btn-secondary">determiniraj</button> 
  <button type="button" class="btn btn-secondary">obrni</button> 
  <button type="button" class="btn btn-secondary">reši sistem</button> 
  
  <div class="btn-group-vertical dropright" role="group">
    <button id="btnGroupDrop1" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      lasntosti matrik
    </button>
    <div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
      <a class="dropdown-item" href="/normalnost">preveri normalnost</a>
      <a class="dropdown-item" href="/simetricnost">preveri simetričnost</a>
      <a class="dropdown-item" href="/ortogonalnost">preveri ortogonalnost</a>
    </div>
  </div>
</div>


