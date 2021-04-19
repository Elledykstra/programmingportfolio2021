//Elle Dykstra| computer Timeline Project
//sept 14,2020
boolean hover;


void setup() {
  size(900, 400);
}

void draw() {
  background(128);
  println(mouseX+ " "+ mouseY);
  drawRef();
  histEvent(100, 215, 100, 20, "Computer Title", "Computer Description blah, blah ,blah",true);
  histEvent(100, 300, 100, 20, "Computer Title", "Computer Description2 blah, blah ,blah",false);
}

void drawRef() {
  // title 
  textAlign(CENTER);
  textSize(50);
  fill(251, 219, 255);
  text("Computer Timeline", width/2, 65);
  line(100, 250, 800, 250);

  //descriptive text

  //Timeline
  stroke(0);
  strokeWeight(5);
  line(100, 250, 800, 250);
  fill(219, 237, 255);

  //decorative elements
}

void histEvent(int x, int y, int w, int h, String title, String description,boolean top) {
  // draw rectangle
  if (hover) {
    fill(0);
    textSize(20);
    text(description, 300, 350);
  } else {
    fill(117, 125, 175);
  }
  fill(117, 125, 175);
  strokeWeight(1);
  rect(x, y, w, h, 5);

  //draw connecting line
  if(top){
      line(x+10, y+20, x+25, y+35);
  } else {
      line(x+10, y+20, x+25, y-35);
  }

  //draw title of the historic event
  textAlign(LEFT);
  textSize(16);
  fill(0);
  text("Title", x+5, y+20);

  //detect the mouse over
  hover = (mouseX > x && mouseX < x+w && mouseY > y && mouseY < y+h);
}
