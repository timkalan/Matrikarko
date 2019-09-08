%rebase ('bootstrap.tpl')
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Matrikulator!</title>
    <link href="https://fonts.googleapis.com/css?family=Amatic+SC|Montserrat&display=swap" rel="stylesheet">
    <style>
            body {
            position: relative;
            height: 100vh;
            margin: 0;
            font-family: 'Montserrat', sans-serif;
            background-color: #FFFFFB}

            .dom {
              padding: 5px;
              margin-top: 25px;
              }

            .form-group {
              adding: 5px;
              margin-top: 25px;
              }

             .center {
              margin-left:auto; 
              margin-right:auto;
              width: 100%;
              text-align: center;
              }

        h1 {40px;padding-top: 25px;}
        footer {font-family: 'Montserrat', sans-serif;position: absolute;bottom: 0;width: 100%;height: 2.5rem;}
    
    </style>
</head>
    <body>
<div class="container">

<div class="mx-auto" style="width: 300px;">
  <h1><a href="/" style="color: #000000;">Matrikulator!</a></h1>
  </div>

<div class="btn-group" role="group" aria-label="Button group with nested dropdown">
  <a href="/sestevanje" class="btn btn-secondary">seštej</a>       
  <a href="/odstevanje" class="btn btn-secondary">odštej</a> 
  <a href="/mnozenje" class="btn btn-secondary">pomnoži</a> 
  <a href="/sledenje" class="btn btn-secondary">sledi</a> 
  <a href="/transponiranje" class="btn btn-secondary">transponiraj</a> 
  <a href="/determiniranje" class="btn btn-secondary">determiniraj</a> 
  <a href="/obracanje" class="btn btn-secondary">obrni</a> 
  <a href="/vektorji" class="btn btn-secondary">uporabi na vektorju</a> 
  <a href="/sistemi" class="btn btn-secondary">reši sistem</a> 
  
  <div class="btn-group-vertical " role="group">
    <button id="btnGroupDrop1" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      lastnosti matrik
    </button>
    <div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
      <a class="dropdown-item" href="/normalnost">preveri normalnost</a>
      <a class="dropdown-item" href="/simetricnost">preveri simetričnost</a>
      <a class="dropdown-item" href="/ortogonalnost">preveri ortogonalnost</a>
    </div>
  </div>
</div>


    {{ !base }}
    </body>