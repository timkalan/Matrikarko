% rebase("osnova")

<form action={{operacija}}>
  <div class="form-group">
    <label for="matrika1">Vpiši prvo matriko:</label>
    <textarea class="form-control" id="matrika1" rows="10" name="matrika1" placeholder="prva matrika"></textarea>

    <div align="center">
      <h1>{{operator}}</h1>
    </div>

    <label for="matrika2">Vpiši drugo matriko:</label>
    <textarea class="form-control" id="matrika2" rows="10" name="matrika2" placeholder="druga matrika"></textarea>
    <input type="submit" value={{operiraj}}!>
  </div>
</form>

