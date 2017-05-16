<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Regexp</title>
    <link rel="stylesheet" href="static/css/style.css" />
  </head>
  <body>
    <h1>One-step authorization</h1>
    <p>
        Logins and passwords are unsecure: everyone can hack it! We invented new, only-password authentication method! Try it now:
    </p>
    <form method="get" action="">
<?php
require 'flag.php';

if (isset ($_GET['password'])) {
  if (ereg("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)
    echo '<p class="error">Only alphanumeric passwords allowed!</p>';
  else if (strpos ($_GET['password'], '--') !== FALSE)
    echo '<p>Flag: '. $flag . '</p>';
  else
    echo '<p class="error">Wrong password</p>';
}
?>
        <p>
            <label for="password">Password: </label>
            <input type="password" name="password" id="password" />
        </p>
        <p>
            <button>Login</button>
        </p>
    </form>
    <hr/>
    <p class="footer">
      Copyright &copy; @nsychev, 2017. This software is <a href="source.txt">fully open-sourced</a> and licensed by MIT
    </p>
  </body>
</html>
