<template>
  <div style="position: relative; display: inline-block;">
    
      <div style="position: absolute; display : flex; width: 100%; align-items: center; padding:20px">
        <!-- Player1 health-->
        <div style="position: relative; height: 30px; width: 100%; display: flex; justify-content: flex-end;">
          <div style="background-color: red; height: 30px;width: 100%"></div>
          <div id="Player1Health" :style="background1"></div>
        </div>
        
        <!-- Clock-->
        <div style="background-color: red; height: 100px; width: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center;">{{timer}}</div>

        <!-- Player2 health-->
        <div style="position: relative; height: 30px; width: 100%">
          <div  style="background-color: red; height: 30px;"></div>
          <div id="Player2Health" :style="background2"></div>
        </div>
        

      </div>
    <div style="position: absolute; color: white; display: flex; align-items: center;justify-content: center;top: 0; left: 0; bottom: 0; right: 0;">{{result}}</div>
    <canvas ref="combat" id="combat" :width="width" :height="height"></canvas>
  </div>
</template>

<script>
import myImage from "./background.png";
export default {
  name: 'combat',
  data() {
    return {    
      width: 1024,
      height: 576,
      background1: "",
      background2: "",
      timer : 10,
      result: ""
    }
  },
  mounted(){
    this.context = this.$refs.combat.getContext("2d");
    this.canvas = document.querySelector("canvas")
    this.timerid
    this.annimationid
    this.drawGame();
    class SpriteBack{
      constructor({position, imageSrc}){
        this.position = position;
        this.height = 150;
        this.width = 50;
        this.image = new Image();
        this.image.src = imageSrc;
      }

    }
    class Sprite{
      constructor({position, velocity}){
        this.health= 100;
        this.attackdmg = 10;
        this.position = position;
        this.velocity = velocity;
        this.height = 150;
        this.width = 50;
        this.lastkey;
        this.attackbox = {
          position : {
            x: this.position.x,
            y: this.position.y
          },
          width : 100,
          height : 50,
        };
        this.isAttacking;
      }

    }
    const background = new SpriteBack({
      position:{
        x:0,
        y:0
      },
      imageSrc : myImage
    })
    const player1 = new Sprite({
      position:{
      x: 0,
      y: 0
    },
    velocity:{
      x:0,
      y:1.2
    }
    })
    const player2 = new Sprite({
      position:{
      x: 400,
      y: 300
    },
    velocity:{
      x:0,
      y:0
    },
    })
    const key= {
      a:{
        pressed : false
      },
      d:{
        pressed: false
      },
      s:{
        pressed: false
      },
      w:{
        pressed: false
      },
      left:{
        pressed : false
      },
      right:{
        pressed: false
      },
      down:{
        pressed: false
      },
      up:{
        pressed: false
      },

    }
    this.background1 = "position: absolute; background: yellow; top: 0; bottom: 0; right: 0; width: "+ player1.health+"%;"
    this.background2 = "position: absolute; background: yellow; top: 0; left: 0; bottom: 0; right: 0; width: "+ player2.health+"%;"
    this.drawBackground(background)
    this.drawPlayer(player1)
    this.drawPlayer(player2)
    this.timerclock(player1,player2)
    this.animation(player1,player2,key,background)

    //Detecting keys
    window.addEventListener('keydown',(event) =>{
      switch(event.key){
        case 'a':
          key.a.pressed = true
          player1.lastkey = 'a'
          break
        case 'd':
          key.d.pressed = true
          player1.lastkey = 'd'
          break
        case 's':
          key.s.pressed = true
          //player1.lastkey = 's'
          break
        case 'w':
          key.w.pressed = true
          player1.velocity.y = -15
          //player1.lastkey = 'w'
          break
        case ' ':
          this.attack(player1)
          break
        case 'ArrowLeft':
          key.left.pressed = true
          player2.lastkey = 'ArrowLeft'
          break
        case 'ArrowRight':
          key.right.pressed = true
          player2.lastkey = 'ArrowRight'
          break
        case 'ArrowDown':
          key.down.pressed = true
          //player2.lastkey = 'ArrowDown'
          break
        case 'ArrowUp':
          key.up.pressed = true
          player2.velocity.y = -15
          //player2.lastkey = 'ArrowUp'
          break
        case '0':
          this.attack(player2)
          break
      }
    })
    window.addEventListener('keyup',(event) =>{
      switch(event.key){
        case 'a':
          key.a.pressed = false
          break
        case 'd':
          key.d.pressed = false
          break
        case 's':
          key.s.pressed = false
          break
        case 'w':
          key.w.pressed = false
          break
        case 'ArrowLeft':
          key.left.pressed = false
          player2.lastkey = 'ArrowLeft'
          break
        case 'ArrowRight':
          key.right.pressed = false
          player2.lastkey = 'ArrowRight'
          break
        case 'ArrowDown':
          key.down.pressed = false
          //player2.lastkey = 'ArrowDown'
          break
        case 'ArrowUp':
          key.up.pressed = false
          player2.velocity.y = -15
          //player2.lastkey = 'ArrowUp'
          break
      }
    })

  },
  methods: {
    drawPlayer: function (player){
      //Draw
      this.context.beginPath();
      this.context.rect(player.position.x,player.position.y,50,player.height);
      this.context.fillStyle = "black";
      this.context.fill();
      this.context.closePath();

      if(player.isAttacking){
        this.context.beginPath();
        this.context.fillStyle = "green";
        this.context.rect(player.attackbox.position.x,player.attackbox.position.y,player.attackbox.width,player.attackbox.height);
        this.context.fill();
        this.context.closePath();

      }
    },
    drawBackground(background){
      this.context.drawImage(background.image, background.position.x, background.position.y)
      
    },
    drawGame(){
      //Clear canvas
      this.context.fillStyle = "grey";
      this.context.fillRect(0,0,this.width,this.height);
    },
    update(Player){
      Player.position.x += Player.velocity.x
      Player.position.y += Player.velocity.y
      this.drawPlayer(Player)
      if  (Player.position.y + Player.velocity.y + Player.height >= this.canvas.height){
        Player.velocity.y=0
      }else{
        Player.velocity.y += 0.5
      }
    },
    attack(player1){
      player1.isAttacking = true
      setTimeout(() => {player1.isAttacking = false}, 100)

    },
    detectcolision(player1,player2){
      return player1.attackbox.position.x + player1.attackbox.width >= player2.position.x 
      && player1.attackbox.position.x <= player2.position.x + player2.width 
      && player1.attackbox.position.y + player1.attackbox.height >= player2.position.y
      && player1.attackbox.position.y <= player2.position.y + player2.height
    },
    Winner(player1,player2){
      clearTimeout(this.timerid)
      if(player1.health == player2.health){
          this.result= "tie"
        }else if(player1.health > player2.health){
          this.result= "Player 1 Win!"
        }else{
          this.result= "Player 2 Win!"
        }
    },
    timerclock(player1,player2){
      if(this.timer>0){
        this.timerid = setTimeout(()=> {this.timerclock(player1,player2)},1000)
        this.timer -- 
      }
      if(this.timer <= 0){
        this.Winner(player1,player2)
      }
      
    },
    animation(player1,player2,key,background){
      this.annimationid = window.requestAnimationFrame(()=> {this.animation(player1,player2,key,background)})

      //Player1 movements
      player1.velocity.x = 0
      player2.velocity.x = 0
      if(key.a.pressed && player1.lastkey == 'a'){
        if( player1.position.x + player1.velocity.x <= 0){
        player1.velocity.x = 0
        }else{
          player1.velocity.x = -5
        }
      }else if(key.d.pressed && player1.lastkey == 'd'){
        if( player1.position.x + player1.velocity.x + player1.width >= this.canvas.width){
        player1.velocity.x = 0
        }else{
          player1.velocity.x = 5
        }
      }
      //Player2 movements
      if(key.left.pressed && player2.lastkey == 'ArrowLeft'){
        if( player2.position.x + player2.velocity.x <= 0){
        player2.velocity.x = 0
        }else{
          player2.velocity.x = -5
        }
      }else if(key.right.pressed && player2.lastkey == 'ArrowRight'){
        if( player2.position.x + player2.velocity.x + player2.width >= this.canvas.width){
        player2.velocity.x = 0
        }else{
          player2.velocity.x = 5
        }
      }
      
      //Attack
      if( this.detectcolision(player1,player2) && player1.isAttacking){
        player1.isAttacking = false
        player2.health -= player1.attackdmg
        this.background2 = "position: absolute; background: yellow; top: 0; left: 0; bottom: 0; right: 0; width: "+ player2.health+"%;"
      }
      if( this.detectcolision(player2,player1) && player2.isAttacking){
        player2.isAttacking = false
        player1.health -= player2.attackdmg
        this.background1 = "position: absolute; background: yellow; top: 0;  bottom: 0; right: 0; width: "+ player1.health+"%;"
      }
      if(player1.position.x > player2.position.x){
        player1.attackbox.position.x = player1.position.x - 50
        player1.attackbox.position.y = player1.position.y
        player2.attackbox.position.x = player2.position.x
        player2.attackbox.position.y = player2.position.y
      }else{
        player1.attackbox.position.x = player1.position.x
        player1.attackbox.position.y = player1.position.y
        player2.attackbox.position.x = player2.position.x - 50
        player2.attackbox.position.y = player2.position.y
      }
      this.drawGame() 
      this.drawBackground(background)
      this.update(player1,background)
      this.update(player2,background)

      if(player1.health <= 0 || player2.health <= 0){
        this.Winner(player1,player2)
        window.cancelAnimationFrame(this.annimationid)
      }


    },

    

  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  *{
    box-sizing: border-box;
  }
 body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }
 #combat {
    border: 1px solid black;
  }
</style>
