% rebase("osnova")

<form action={{ operacija }} method="POST">
  <div class="form-group">
    <h3><label for="matrika1">Vpiši prvo matriko:</label></h3>
    <textarea class="form-control" id="matrika1" rows="10" name="matrika1" placeholder="prva matrika"></textarea>

    <div align="center">
      <h1>{{ operator }}</h1>
    </div>

    <h3><label for="matrika2">Vpiši drugo matriko:</label></h3>
    <textarea class="form-control" id="matrika2" rows="10" name="matrika2" placeholder="druga matrika"></textarea>
    <input type="submit" value={{ operiraj }}!>
  </div>
</form>

