let list_of_types = ['normal', 'plante', 'feu', 'eau', 'electrik', 'glace', 'combat', 'poison', 'sol', 'vol', 'psy', 'insecte', 'roche', 'spectre', 'dragon', 'tenebres', 'acier', 'fee', 'aucun'];
let list_of_weaknesses = [
    [1,1,1,1,1,1,2,1,1,1,1,1,1,0,1,1,1,1], 
    [1,0.5,2,0.5,0.5,2,1,2,0.5,2,1,2,1,1,1,1,0.5,0.5],
    [1,0.5,0.5,2,1,0.5,1,1,2,1,1,0.5,1,1,1,1,0.5,1],
    [1,2,0.5,0.5,2,0.5,1,1,1,1,1,1,1,1,1,1,0.5,1],
    [1,1,1,1,0.5,1,1,1,2,0.5,1,1,1,1,1,1,0.5,1],
    [1,1,2,1,1,0.5,2,1,1,1,1,1,2,1,1,1,2,1],
    [1,1,1,1,1,1,1,1,1,2,2,0.5,0.5,1,1,0.5,1,2],
    [1,0.5,1,1,1,1,0.5,0.5,2,1,2,0.5,1,1,1,1,1,0.5],
    [1,2,1,2,0,2,1,0.5,1,1,1,1,0.5,1,1,1,1,1],
    [1,0.5,1,1,2,2,0.5,1,0,1,1,0.5,2,1,1,1,1,1],
    [1,1,1,1,1,1,0.5,1,1,1,0.5,2,1,2,1,2,1,1],
    [1,0.5,2,1,1,1,0.5,1,0.5,2,1,1,2,1,1,1,1,1],
    [0.5,2,0.5,2,1,1,2,0.5,2,0.5,1,1,1,1,1,1,2,1],
    [0,1,1,1,1,1,0,0.5,1,1,1,0.5,1,2,1,2,1,1],
    [1,0.5,0.5,0.5,0.5,2,1,1,1,1,1,1,1,1,2,1,1,2],
    [1,1,1,1,1,1,2,1,1,1,0,2,1,0.5,1,0.5,1,2],
    [0.5,0.5,2,1,1,0.5,2,0,2,0.5,0.5,0.5,0.5,1,0.5,1,0.5,0.5],
    [1,1,1,1,1,1,0.5,2,1,1,1,0.5,1,1,0,0.5,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
  ];


function calculateAndDisplayWeaknesses() {
    let type1 = document.getElementById('type1').value;
    let type2 = document.getElementById('type2').value;
  
    let type1Index = list_of_types.indexOf(type1);
    let type2Index = list_of_types.indexOf(type2);
  
    if (type1Index === -1 || type2Index === -1) {
      document.getElementById('output').innerHTML = "Type inconnu. Veuillez réessayer.";
      return;
    }
  
    let type1Weaknesses = list_of_weaknesses[type1Index];
    let type2Weaknesses = list_of_weaknesses[type2Index];
  
    let immunity_list = [];
    let double_resistance_list = [];
    let resistance_list = [];
    let weakness_list = [];
    let double_weakness_list = [];
  
    for (let i = 0; i < list_of_types.length; i++) {
      let weakness = type1Weaknesses[i] * type2Weaknesses[i];
      if (weakness === 0) {
        immunity_list.push(list_of_types[i]);
      } else if (weakness === 0.25) {
        double_resistance_list.push(list_of_types[i]);
      } else if (weakness === 0.5) {
        resistance_list.push(list_of_types[i]);
      } else if (weakness === 2) {
        weakness_list.push(list_of_types[i]);
      } else if (weakness === 4) {
        double_weakness_list.push(list_of_types[i]);
      }
    }
  
    let output = "";
    if (double_weakness_list.length > 0) {
      output += "Double(s) faiblesse(s) : " + double_weakness_list.join(", ") + "<br>";
    }
    if (weakness_list.length > 0) {
      output += "Faiblesse(s) : " + weakness_list.join(", ") + "<br>";
    }
    if (double_resistance_list.length > 0) {
      output += "Double(s) résistance(s) : " + double_resistance_list.join(", ") + "<br>";
    }
    if (resistance_list.length > 0) {
      output += "Résistance(s) : " + resistance_list.join(", ") + "<br>";
    }
    if (immunity_list.length > 0) {
      output += "Immunité(s) : " + immunity_list.join(", ") + "<br>";
    }
  
    document.getElementById('output').innerHTML = output;
  }