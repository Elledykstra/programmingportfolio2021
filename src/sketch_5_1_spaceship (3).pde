void setup() {
  size(500,500);
}

void draw() {
  background(0);
  display(mouseX, mouseY);
}

void display(int x, int y) {
  rectMode(CENTER);
  fill(126,1,1);
  stroke(80);
  rect(x-25,y+25,15,15);
  rect(x+25,y+25,15,15);
  line(x-30,y-15,x-30,y+5);
  line(x+30,y-15,x+30,y+5);
  fill(193,113,115);
  triangle(x,y-50,x+45,y+20,x-45,y+20);
  fill(100,35,20);
  triangle(x,y-30,x+35,y+20,x-35,y+20);
  ellipse(x,y,20,78);
  fill(193,204,255);
  rect(x,y,15,35);
  fill(38,50,252);
  stroke(100);
  ellipse(x,y,10,27);
}
