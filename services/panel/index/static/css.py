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
  color: palevioletred;
}
.round-corners {
  border-radius: 5px;
}
blockquote {
  border-left: 5px solid rgb(127, 255, 212, 0.2);
  padding-left: 15px;
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
  color: palevioletred;
  opacity: 50%;
}
blockquote .fas {
  color: rgb(127, 255, 212, 0.5);
}
"""

