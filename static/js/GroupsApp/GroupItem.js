var React = require("react");


module.exports = React.createClass({
	render:function(){
		var group = this.props.group;
		var detail_link = '#/group/'+group.id;
		return(
			<div className="col-md-4">
				<div>
					<div className="thumbnail entity">
						<div className="img-box">
                                <a href={detail_link}>
                                    <img  src={group.img} className="img-responsive img-rounded" alt="Responsive image"/>
                                </a>
                        </div>

                        <div className="col-md-12">
                                <p className="title">{group.title}</p>
                        </div>


                        <div className="col-md-6">
                                <p className="number">{group.amount}</p>
                        </div>

                        <div className="col-md-6">
                                <p className="number">{group.unit_price}</p>
                        </div>

                        <div className="col-md-6">
                                <p className="number">限价</p>

                        </div>
                        <div className="col-md-6">
                                <p className="number">限重</p>
                                
                        </div>
					</div>
				</div>
			</div>
		)		
	}
})