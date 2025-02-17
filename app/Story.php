<?php

namespace App;

use Illuminate\Database\Eloquent\Model;
use App\User;
use App\Comment;

class Story extends Model
{
    //
    protected $table = 'stories';
    public $primarykey = 'id';

    public function user(){
        return $this->belongsTo('App/User');
    }
    public function comments(){
        return $this->hasMany('App\Comment');
    }
}
