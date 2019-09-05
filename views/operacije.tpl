% rebase("osnova")

<form action={{operacija}}>
  <div class="form-group">
    <label for="matrika1">Matrika 1:</label>
    <textarea class="form-control" id="matrika1" rows="10" name="matrika1"></textarea>
    <textarea class="form-control" id="matrika2" rows="10" name="matrika2"></textarea>
    <input type="submit" value="SEŠTEJ!">
  </div>
</form>

<div>
  <h1>{{operator}}</h1>
</div>

