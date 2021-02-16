css = """
body {
  background-color: #292929;
  color: white;
  margin: 2em;
}
h1, h2 {
  font-family: 'Hack', monospace;
  font-weight: 500;
  margin-bottom: 0;
}
ul {
  list-style-type: none;
}
p {
  font-family: 'Nunito', sanserif;
}
#description > a {
  font-family: 'Hack', monospace;
  font-size: 110%;
}
.round-corners {
  border-radius: 5px;
}
blockquote {
  border-left: 5px solid rgb(127, 255, 212, 0.2);
  background-color: rgb(127, 255, 212, 0.1);
  padding: 15px;
}
img {
  margin-top: 5px;
}
.change-icon > .fas + .fas,
.change-icon:hover > .fas {
  display: none;
}
.change-icon:hover > .fas + .fas {
  display: inherit;
  opacity: 80%;
}
.fas {
  color: rgb(127, 255, 212, 0.7);
  cursor: pointer;
}
blockquote .fas {
  color: rgb(127, 255, 212, 0.5);
}
p#description i {
  opacity: 100%;
  color: white;
}
.visible {
  display: block;
}
.invisible {
  display: none;
}
.title {
  color: white;
  font-family: 'Hack', monospace;
  cursor: pointer;
}
a.txt:link,
a.txt:visited {
    border-bottom: 1px dashed;
    color: palevioletred;
    font-style: normal;
    font-weight: 400;
    text-decoration: none;
}
a.txt:hover,
a.txt:focus {
    border-bottom-style: solid;
    color: khaki;
    outline: 1px solid;
    outline-offset: .125em;
}

"""

