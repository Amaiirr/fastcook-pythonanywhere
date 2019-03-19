var itemID;


//allows the user to drop to another section
function allowDrop(ev)
{
	ev.preventDefault();
}

function dragStart(ev)
{
	itemID = ev.target.id;
}

function drop(ev)
{
	ev.target.append(document.getElementById(itemID));

}

function test(ev) {
    			ev.draggable();
  			} 
