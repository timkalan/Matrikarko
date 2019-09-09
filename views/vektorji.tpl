% rebase("osnova")

<form action={{ kater }} method="POST">
<h4 style="margin-top: 25px">{{ opis }}</h4>
  <div class="form-group">
    <h3><label for="matrika">{{ kaj1 }}</label></h3>
    <textarea class="form-control" id="matrika" rows="10" name="matrika" placeholder="matrika"></textarea>
    <h3><label for="vektor" style="margin-top: 20px">{{ kaj2 }}</label></h3>
    <input type="vektor" class="form-control" id="vektor" name="vektor" placeholder="vektor">
    <input type="submit" value="{{ delaj }}!">
  </div>
</form>
